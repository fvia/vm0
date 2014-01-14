# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Items.weight'
        db.delete_column(u'app0_items', 'weight')


    def backwards(self, orm):
        # Adding field 'Items.weight'
        db.add_column(u'app0_items', 'weight',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
        u'app0.items': {
            'Meta': {'object_name': 'Items'},
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_date': ('django.db.models.fields.DateTimeField', [], {}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'person_ref': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['app0']