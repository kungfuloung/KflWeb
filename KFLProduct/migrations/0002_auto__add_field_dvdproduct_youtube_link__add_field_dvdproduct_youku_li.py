# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DVDProduct.youtube_link'
        db.add_column('KFLProduct_dvdproduct', 'youtube_link',
                      self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True),
                      keep_default=False)

        # Adding field 'DVDProduct.youku_link'
        db.add_column('KFLProduct_dvdproduct', 'youku_link',
                      self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True),
                      keep_default=False)

        # Adding field 'DVDProduct.taobao_link'
        db.add_column('KFLProduct_dvdproduct', 'taobao_link',
                      self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True),
                      keep_default=False)

        # Adding field 'DVDProduct.paypal_button'
        db.add_column('KFLProduct_dvdproduct', 'paypal_button',
                      self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DVDProduct.youtube_link'
        db.delete_column('KFLProduct_dvdproduct', 'youtube_link')

        # Deleting field 'DVDProduct.youku_link'
        db.delete_column('KFLProduct_dvdproduct', 'youku_link')

        # Deleting field 'DVDProduct.taobao_link'
        db.delete_column('KFLProduct_dvdproduct', 'taobao_link')

        # Deleting field 'DVDProduct.paypal_button'
        db.delete_column('KFLProduct_dvdproduct', 'paypal_button')


    models = {
        'KFLProduct.dvdproduct': {
            'Meta': {'object_name': 'DVDProduct'},
            'discription_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'discription_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['KFLProduct']