# -*- coding: utf-8 -*-
import logging
import os
import warnings
import tempfile
import shutil
import json

from subprocess import check_call
from tarfile import TarFile
from pkgutil import get_data
from io import BytesIO
from contextlib import closing

from europarse.tz import tzfile

__all__ = ["gettz", "gettz_db_metadata", "rebuild"]

ZONEFILENAME = "europarse-zoneinfo.tar.gz"
METADATA_FN = 'METADATA'


class tzfile(tzfile):
    def __reduce__(self):
        return (gettz, (self._filename,))


def getzoneinfofile_stream():
    try:
        return BytesIO(get_data(__name__, ZONEFILENAME))
    except IOError as e:  # TODO  switch to FileNotFoundError?
        warnings.warn("I/O error({0}): {1}".format(e.errno, e.strerror))
        return None


class ZoneInfoFile(object):
    def __init__(self, zonefile_stream=None):
        if zonefile_stream is not None:
            with TarFile.open(fileobj=zonefile_stream, mode='r') as tf:
                self.zones = {
                    zf.name: tzfile(tf.extractfile(zf), filename=zf.name)
                    for zf in tf.getmembers()
                    if zf.isfile() and zf.name != METADATA_FN
                }
                # deal with links: They'll point to their parent object. Less
                # waste of memory
                # links = {zl.name: self.zones[zl.linkname]
                #        for zl in tf.getmembers() if zl.islnk() or zl.issym()}
                links = dict((zl.name, self.zones[zl.linkname])
                             for zl in tf.getmembers() if
                             zl.islnk() or zl.issym())
                self.zones.update(links)
                try:
                    metadata_json = tf.extractfile(tf.getmember(METADATA_FN))
                    metadata_str = metadata_json.read().decode('UTF-8')
                    self.metadata = json.loads(metadata_str)
                except KeyError:
                    # no metadata in tar file
                    self.metadata = None
        else:
            self.zones = dict()
            self.metadata = None


# The current API has gettz as a module function, although in fact it taps into
# a stateful class. So as a workaround for now, without changing the API, we
# will create a new "global" class instance the first time a user requests a
# timezone. Ugly, but adheres to the api.
#
# TODO: deprecate this.
_CLASS_ZONE_INSTANCE = list()


def gettz(name):
    if len(_CLASS_ZONE_INSTANCE) == 0:
        _CLASS_ZONE_INSTANCE.append(ZoneInfoFile(getzoneinfofile_stream()))
    return _CLASS_ZONE_INSTANCE[0].zones.get(name)


def gettz_db_metadata():
    """ Get the zonefile metadata

    See `zonefile_metadata`_

    :returns: A dictionary with the database metadata
    """
    if len(_CLASS_ZONE_INSTANCE) == 0:
        _CLASS_ZONE_INSTANCE.append(ZoneInfoFile(getzoneinfofile_stream()))
    return _CLASS_ZONE_INSTANCE[0].metadata


