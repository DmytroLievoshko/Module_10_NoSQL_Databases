from datetime import datetime
import validator as validator

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import DateTimeField, EmbeddedDocumentField, ListField, StringField, IntField


ContactInformationTypes = {1: {"name": "Address"},
                           2: {"name": "Phone", "validator": validator.phone_check},
                           3: {"name": "Email", "validator": validator.email_check}}


class KeyWord(EmbeddedDocument):
    name = StringField()


class Note(Document):
    description = StringField()
    created = DateTimeField(default=datetime.now())
    keyWords = ListField(EmbeddedDocumentField(KeyWord))

    def __str__(self):
        return f"{self.description} --created: {self.created} --keywords: {', '.join([keyWord.name for keyWord in self.keyWords])}"


class ContactInformation(EmbeddedDocument):
    contactInformationType = IntField()
    description = StringField()

    def __str__(self):
        return f"{ContactInformationTypes.get(self.contactInformationType).get('name')} {self.description}"


class Person(Document):
    name = StringField()
    birthday = DateTimeField(default=datetime.now())
    contactInformation = ListField(EmbeddedDocumentField(ContactInformation))

    def __str__(self):
        str_erson = f"{self.name} birthday: {self.birthday.strftime('%d-%m-%Y')}"
        for Contact_information in self.contactInformation:
            str_erson += f"\n{Contact_information}"
        return str_erson
