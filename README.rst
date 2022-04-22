europarse - dateutil.parser, but not broken
===========================================

Once upon a time, the dateutil library had a very nice date parsing module that
could be configured to interpret ambiguous xx/xx/xxxx dates as either
dd/mm/yyyy or mm/dd/yyyy depending on the `dayfirst` option. Unfortunately,
in the time-honoured tradition of developers tasked with maintaining a boring
package that just works, they refactored it, and broke it so that passing
`dayfirst=True` causes ISO 8601 xxxx-xx-xx dates to be interpreted as
yyyy-dd-mm, a convention used by literally nobody. Indeed, the fact that
literally nobody uses it is the whole basis of ISO 8601.

https://github.com/dateutil/dateutil/issues/402

Despite this bug making the module essentially useless for the 95% of the
world's population that doesn't use mm/dd/yyyy format, it's apparently not been
worth fixing for the last 5 years.

europarse is a fork of the last good version of dateutil.parser.
