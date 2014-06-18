# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ThreadCategory.rid'
        db.add_column('Discussion_threadcategory', 'rid',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ThreadCategory.rid'
        db.delete_column('Discussion_threadcategory', 'rid')


    models = {
        'Discussion.reply': {
            'Content': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True', 'max_length': '10000'}),
            'Meta': {'object_name': 'Reply'},
            'following_reply': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['Discussion.Reply']", 'null': 'True'}),
            'following_thread': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['Discussion.Thread']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['KFLProduct.UserProfile']", 'null': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'})
        },
        'Discussion.thread': {
            'Meta': {'object_name': 'Thread'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['Discussion.ThreadCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        },
        'Discussion.threadcategory': {
            'Meta': {'object_name': 'ThreadCategory'},
            'discription_CN': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True', 'max_length': '10000'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True', 'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'rid': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'})
        },
        'Discussion.threadcontent': {
            'Content': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True', 'max_length': '10000'}),
            'Meta': {'object_name': 'ThreadContent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['KFLProduct.Language']", 'null': 'True'}),
            'of_thread': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['Discussion.Thread']"}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['KFLProduct.UserProfile']", 'null': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'related_thread': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['Discussion.ThreadContent']", 'null': 'True', 'related_name': "'related_thread_rel_+'"}),
            'replied_by_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '400'})
        },
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '60'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['KFLProduct.ProductCategory']", 'null': 'True'}),
            'discription_CN': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True', 'max_length': '10000'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True', 'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.Language']", 'null': 'True', 'symmetrical': 'False'}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.downloadProduct']", 'null': 'True', 'symmetrical': 'False'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'paypal_button_on_sale': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'price_on_sale': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        },
        'KFLProduct.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'name_en': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'customer_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']"}),
            'last_viewed_product': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.DVDProduct']", 'null': 'True', 'symmetrical': 'False', 'related_name': "'v_product'"}),
            'purchased_product': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.DVDProduct']", 'null': 'True', 'symmetrical': 'False', 'related_name': "'p_product'"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
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
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Discussion']