# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DVDProduct.profile_pic'
        db.delete_column('KFLProduct_dvdproduct', 'profile_pic')

        # Adding field 'DVDProduct.product_image'
        db.add_column('KFLProduct_dvdproduct', 'product_image',
                      self.gf('django.db.models.fields.files.ImageField')(default='ll', blank=True, max_length=100),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'DVDProduct.profile_pic'
        raise RuntimeError("Cannot reverse this migration. 'DVDProduct.profile_pic' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'DVDProduct.profile_pic'
        db.add_column('KFLProduct_dvdproduct', 'profile_pic',
                      self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100),
                      keep_default=False)

        # Deleting field 'DVDProduct.product_image'
        db.delete_column('KFLProduct_dvdproduct', 'product_image')


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
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.ProductCategory']", 'blank': 'True', 'null': 'True'}),
            'discription_CN': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']", 'blank': 'True', 'null': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.downloadProduct']", 'null': 'True'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'paypal_button_on_sale': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'price_on_sale': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'})
        },
        'KFLProduct.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.productbundle': {
            'Meta': {'object_name': 'ProductBundle'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.ProductCategory']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'percent_off': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.DVDProduct']", 'null': 'True'})
        },
        'KFLProduct.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.productcomment': {
            'Content': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'Meta': {'object_name': 'ProductComment'},
            'following_comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.ProductComment']", 'blank': 'True', 'null': 'True'}),
            'following_product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.DVDProduct']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.UserProfile']", 'blank': 'True', 'null': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'customer_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']"}),
            'last_viewed_product': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.DVDProduct']", 'related_name': "'v_product'", 'null': 'True'}),
            'purchased_product': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.DVDProduct']", 'related_name': "'p_product'", 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['KFLProduct']