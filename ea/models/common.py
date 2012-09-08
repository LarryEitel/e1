from structures.models import EmbeddedModel
from structures.types import (StringType, DateTimeType, EmailType)
from structures.types.mongo import ObjectIdType

class Email(EmbeddedModel):
    if 1: # Fields
        email  = EmailType()
    if 1: # Methods
        def __unicode__(self):
            return self.email

class Log(EmbeddedModel):
    if 1: # Fields
        oBy  = ObjectIdType()
        oOn  = DateTimeType(required=True) # ObjectIdType()
        oLoc = StringType()
        cOn  = DateTimeType()
        cBy  = ObjectIdType()
        cLoc = StringType()
        mOn  = DateTimeType()
        mBy  = ObjectIdType()
        mLoc = StringType()
        dBy  = ObjectIdType()
        dOn  = DateTimeType()
        dLoc = StringType()
        note = StringType()
    if 1: # Methods
        def __unicode__(self):
            return str(self.cOn)
