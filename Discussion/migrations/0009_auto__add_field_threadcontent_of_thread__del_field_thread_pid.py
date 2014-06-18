# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ThreadContent.of_thread'
        db.add_column('Discussion_threadcontent', 'of_thread',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Discussion.Thread'], default='', blank=True),
                      keep_default=False)

        # Deleting field 'Thread.pid'
        db.delete_column('Discussion_thread', 'pid')


    def backwards(self, orm):
        # Deleting field 'ThreadContent.of_thread'
        db.delete_column('Discussion_threadcontent', 'of_thread_id')

        # Adding field 'Thread.pid'
        db.add_column('Discussion_thread', 'pid',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    models = {
        'Discussion.reply': {
            'Content': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'Meta': {'object_name': 'Reply'},
            'following_reply': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['Discussion.Reply']", 'blank': 'True'}),
            'following_thread': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['Discussion.Thread']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['KFLProduct.UserProfile']", 'blank': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'Discussion.thread': {
            'Meta': {'object_name': 'Thread'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Discussion.ThreadCategory']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'})
        },
        'Discussion.threadcategory': {
            'Meta': {'object_name': 'ThreadCategory'},
            'discription_CN': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'})
        },
        'Discussion.threadcontent': {
            'Content': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'Meta': {'object_name': 'ThreadContent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['KFLProduct.Language']", 'blank': 'True'}),
            'of_thread': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Discussion.Thread']", 'blank': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['KFLProduct.UserProfile']", 'blank': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'related_thread': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_thread_rel_+'", 'null': 'True', 'to': "orm['Discussion.ThreadContent']", 'blank': 'True'}),
            'replied_by_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '400', 'blank': 'True'})
        },
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '60', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['KFLProduct.ProductCategory']", 'blank': 'True'}),
            'discription_CN': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.Language']", 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.downloadProduct']", 'blank': 'True'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'paypal_button_on_sale': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'price_on_sale': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'})
        },
        'KFLProduct.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'customer_number': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']"}),
            'last_viewed_product': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'v_product'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.DVDProduct']", 'blank': 'True'}),
            'purchased_product': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'p_product'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['KFLProduct.DVDProduct']", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Discussion']