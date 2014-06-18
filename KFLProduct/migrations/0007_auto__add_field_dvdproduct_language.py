# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DVDProduct.language'
        db.add_column('KFLProduct_dvdproduct', 'language',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['KFLProduct.Language'], blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DVDProduct.language'
        db.delete_column('KFLProduct_dvdproduct', 'language_id')


    models = {
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['KFLProduct.ProductCategory']", 'blank': 'True'}),
            'discription_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '10000'}),
            'discription_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['KFLProduct.Language']", 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['KFLProduct.downloadProduct']", 'blank': 'True', 'symmetrical': 'False'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'KFLProduct.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'KFLProduct.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['KFLProduct']