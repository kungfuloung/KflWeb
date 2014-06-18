# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DVDProduct'
        db.create_table('KFLProduct_dvdproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(null=True, max_length=30, blank=True)),
            ('title_CN', self.gf('django.db.models.fields.CharField')(null=True, max_length=30, blank=True)),
            ('title_EN', self.gf('django.db.models.fields.CharField')(null=True, max_length=30, blank=True)),
            ('discription_CN', self.gf('django.db.models.fields.CharField')(null=True, max_length=10000, blank=True)),
            ('discription_EN', self.gf('django.db.models.fields.CharField')(null=True, max_length=10000, blank=True)),
        ))
        db.send_create_signal('KFLProduct', ['DVDProduct'])


    def backwards(self, orm):
        # Deleting model 'DVDProduct'
        db.delete_table('KFLProduct_dvdproduct')


    models = {
        'KFLProduct.dvdproduct': {
            'Meta': {'object_name': 'DVDProduct'},
            'discription_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'discription_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['KFLProduct']