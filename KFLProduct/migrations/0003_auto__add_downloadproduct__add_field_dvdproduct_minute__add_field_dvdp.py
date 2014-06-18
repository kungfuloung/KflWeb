# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'downloadProduct'
        db.create_table('KFLProduct_downloadproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30, null=True)),
            ('section_no', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('link', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('minute', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('second', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('price', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
        ))
        db.send_create_signal('KFLProduct', ['downloadProduct'])

        # Adding field 'DVDProduct.minute'
        db.add_column('KFLProduct_dvdproduct', 'minute',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'DVDProduct.second'
        db.add_column('KFLProduct_dvdproduct', 'second',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'DVDProduct.price'
        db.add_column('KFLProduct_dvdproduct', 'price',
                      self.gf('django.db.models.fields.FloatField')(blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'downloadProduct'
        db.delete_table('KFLProduct_downloadproduct')

        # Deleting field 'DVDProduct.minute'
        db.delete_column('KFLProduct_dvdproduct', 'minute')

        # Deleting field 'DVDProduct.second'
        db.delete_column('KFLProduct_dvdproduct', 'second')

        # Deleting field 'DVDProduct.price'
        db.delete_column('KFLProduct_dvdproduct', 'price')


    models = {
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'Meta': {'object_name': 'DVDProduct'},
            'discription_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'discription_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['KFLProduct']