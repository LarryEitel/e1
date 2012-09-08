from structures.models import Model, EmbeddedModel
from structures.types import (StringType, IntType, DateTimeType, EmailType)
from structures.types.compound import (ListType, EmbeddedModelType)
from structures.types.mongo import ObjectIdType
from bson import ObjectId
from common import Log, Email

class Contact(Model):       
    shares = ListType(ObjectIdType(ObjectId))
    log    = EmbeddedModelType(Log)
    dnam   = StringType()
    emails = ListType(EmbeddedModelType(Email))

    meta   = {
        'collection': 'contacts'
        }

    def onUpdate(self):
        self.shares = [ObjectId('50468de92558713d84b03fd7')]

    def __unicode__(self):
        if not self.log:
            return self.dnam

class Company(Contact):  
    cnam = StringType()

    meta = {
        'collection': 'contacts'
        } 

    def onUpdate(self):
        super(Company, self).onUpdate()
        self.dnam = self.cnam

class Person(Contact):  
    title  = StringType()
    fnam   = StringType()
    fnam2  = StringType()
    lnam   = StringType()
    lnam2  = StringType()
    suffix = StringType()

    meta = {
        'collection': 'contacts'
        } 

    def onUpdate(self):
        super(Person, self).onUpdate()
        dnam = ''
        fnam = ''
        fnam += self.title + ' ' if self.title else ''
        fnam += self.fnam + ' ' if self.fnam else ''
        fnam += self.fnam2 + ' ' if self.fnam2 else ''
        fnam = fnam[:-1] if fnam else ''

        lnam = ''
        lnam += self.lnam + ' ' if self.lnam else ''
        lnam += self.lnam2 + ' ' if self.lnam2 else ''
        lnam += self.suffix + ' ' if self.suffix else ''
        lnam = lnam[:-1] if lnam else ''

        if lnam: 
            dnam += lnam
            if fnam: 
                dnam += ', ' + fnam
        elif fnam: 
            dnam += fnam
        self.dnam = dnam

class User(Person):  
    unam  = StringType()

    meta = {
        'collection': 'contacts'
        } 

    def onUpdate(self):
        super(User, self).onUpdate()


