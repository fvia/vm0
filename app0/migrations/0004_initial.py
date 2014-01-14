# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Items'
        db.create_table(u'app0_items', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('person_ref', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('person_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'app0', ['Items'])


    def backwards(self, orm):
        # Deleting model 'Items'
        db.delete_table(u'app0_items')


    models = {
        u'app0.items': {
            'Meta': {'object_name': 'Items'},
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_date': ('django.db.models.fields.DateTimeField', [], {}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'person_ref': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['app0']