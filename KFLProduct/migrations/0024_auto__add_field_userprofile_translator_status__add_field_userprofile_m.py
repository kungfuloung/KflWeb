# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserProfile.translator_status'
        db.add_column('KFLProduct_userprofile', 'translator_status',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserProfile.master_status'
        db.add_column('KFLProduct_userprofile', 'master_status',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserProfile.translator_status'
        db.delete_column('KFLProduct_userprofile', 'translator_status')

        # Deleting field 'UserProfile.master_status'
        db.delete_column('KFLProduct_userprofile', 'master_status')


    models = {
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['KFLProduct.ProductCategory']"}),
            'discription_CN': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True', 'null': 'True'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'null': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.Language']"}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'null': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.downloadProduct']"}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'paypal_button_on_sale': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'price_on_sale': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.productbundle': {
            'Meta': {'object_name': 'ProductBundle'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'null': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.ProductCategory']"}),
            'discription_CN': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True', 'null': 'True'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'null': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.Language']"}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'paypal_button_on_sale': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'percent_off': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'null': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.DVDProduct']"}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.productcomment': {
            'Content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True', 'null': 'True'}),
            'Meta': {'object_name': 'ProductComment'},
            'following_comment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['KFLProduct.ProductComment']"}),
            'following_product': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['KFLProduct.DVDProduct']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['KFLProduct.UserProfile']"}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'customer_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']"}),
            'last_viewed_product': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'null': 'True', 'related_name': "'v_product'", 'symmetrical': 'False', 'to': "orm['KFLProduct.DVDProduct']"}),
            'master_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'purchased_product': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'null': 'True', 'related_name': "'p_product'", 'symmetrical': 'False', 'to': "orm['KFLProduct.DVDProduct']"}),
            'translator_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['KFLProduct']