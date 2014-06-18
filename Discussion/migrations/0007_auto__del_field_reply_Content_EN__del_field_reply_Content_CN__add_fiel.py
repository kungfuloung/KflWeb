# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Reply.Content_EN'
        db.delete_column('Discussion_reply', 'Content_EN')

        # Deleting field 'Reply.Content_CN'
        db.delete_column('Discussion_reply', 'Content_CN')

        # Adding field 'Reply.Content'
        db.add_column('Discussion_reply', 'Content',
                      self.gf('django.db.models.fields.TextField')(max_length=10000, blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Thread.topic_CN'
        db.delete_column('Discussion_thread', 'topic_CN')

        # Deleting field 'Thread.translated'
        db.delete_column('Discussion_thread', 'translated')

        # Deleting field 'Thread.Content_EN'
        db.delete_column('Discussion_thread', 'Content_EN')

        # Deleting field 'Thread.Content_CN'
        db.delete_column('Discussion_thread', 'Content_CN')

        # Deleting field 'Thread.topic_EN'
        db.delete_column('Discussion_thread', 'topic_EN')

        # Adding field 'Thread.topic'
        db.add_column('Discussion_thread', 'topic',
                      self.gf('django.db.models.fields.CharField')(max_length=400, blank=True, null=True),
                      keep_default=False)

        # Adding field 'Thread.Content'
        db.add_column('Discussion_thread', 'Content',
                      self.gf('django.db.models.fields.TextField')(max_length=10000, blank=True, null=True),
                      keep_default=False)

        # Adding field 'Thread.in_language'
        db.add_column('Discussion_thread', 'in_language',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['KFLProduct.Language'], blank=True, null=True),
                      keep_default=False)

        # Adding M2M table for field translated_thread on 'Thread'
        m2m_table_name = db.shorten_name('Discussion_thread_translated_thread')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_thread', models.ForeignKey(orm['Discussion.thread'], null=False)),
            ('to_thread', models.ForeignKey(orm['Discussion.thread'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_thread_id', 'to_thread_id'])

        # Adding M2M table for field related_thread on 'Thread'
        m2m_table_name = db.shorten_name('Discussion_thread_related_thread')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_thread', models.ForeignKey(orm['Discussion.thread'], null=False)),
            ('to_thread', models.ForeignKey(orm['Discussion.thread'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_thread_id', 'to_thread_id'])


    def backwards(self, orm):
        # Adding field 'Reply.Content_EN'
        db.add_column('Discussion_reply', 'Content_EN',
                      self.gf('django.db.models.fields.TextField')(max_length=10000, blank=True, null=True),
                      keep_default=False)

        # Adding field 'Reply.Content_CN'
        db.add_column('Discussion_reply', 'Content_CN',
                      self.gf('django.db.models.fields.TextField')(max_length=10000, blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Reply.Content'
        db.delete_column('Discussion_reply', 'Content')

        # Adding field 'Thread.topic_CN'
        db.add_column('Discussion_thread', 'topic_CN',
                      self.gf('django.db.models.fields.CharField')(max_length=400, blank=True, null=True),
                      keep_default=False)

        # Adding field 'Thread.translated'
        db.add_column('Discussion_thread', 'translated',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Thread.Content_EN'
        db.add_column('Discussion_thread', 'Content_EN',
                      self.gf('django.db.models.fields.TextField')(max_length=10000, blank=True, null=True),
                      keep_default=False)

        # Adding field 'Thread.Content_CN'
        db.add_column('Discussion_thread', 'Content_CN',
                      self.gf('django.db.models.fields.TextField')(max_length=10000, blank=True, null=True),
                      keep_default=False)

        # Adding field 'Thread.topic_EN'
        db.add_column('Discussion_thread', 'topic_EN',
                      self.gf('django.db.models.fields.CharField')(max_length=400, blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Thread.topic'
        db.delete_column('Discussion_thread', 'topic')

        # Deleting field 'Thread.Content'
        db.delete_column('Discussion_thread', 'Content')

        # Deleting field 'Thread.in_language'
        db.delete_column('Discussion_thread', 'in_language_id')

        # Removing M2M table for field translated_thread on 'Thread'
        db.delete_table(db.shorten_name('Discussion_thread_translated_thread'))

        # Removing M2M table for field related_thread on 'Thread'
        db.delete_table(db.shorten_name('Discussion_thread_related_thread'))


    models = {
        'Discussion.reply': {
            'Content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True', 'null': 'True'}),
            'Meta': {'object_name': 'Reply'},
            'following_reply': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Discussion.Reply']", 'blank': 'True', 'null': 'True'}),
            'following_thread': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Discussion.Thread']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.UserProfile']", 'blank': 'True', 'null': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'})
        },
        'Discussion.thread': {
            'Content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True', 'null': 'True'}),
            'Meta': {'object_name': 'Thread'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']", 'blank': 'True', 'null': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.UserProfile']", 'blank': 'True', 'null': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'related_thread': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_thread_rel_+'", 'to': "orm['Discussion.Thread']", 'blank': 'True', 'null': 'True'}),
            'replied_by_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True', 'null': 'True'}),
            'translated_thread': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'translated_thread_rel_+'", 'to': "orm['Discussion.Thread']", 'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.ProductCategory']", 'blank': 'True', 'null': 'True'}),
            'discription_CN': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True', 'null': 'True'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']", 'blank': 'True', 'null': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['KFLProduct.downloadProduct']", 'blank': 'True', 'null': 'True'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'paypal_button_on_sale': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'price_on_sale': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'KFLProduct.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'customer_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']"}),
            'last_viewed_product': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['KFLProduct.DVDProduct']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'v_product'", 'null': 'True'}),
            'purchased_product': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['KFLProduct.DVDProduct']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'p_product'", 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Discussion']