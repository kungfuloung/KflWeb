# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ThreadCategory'
        db.create_table('Discussion_threadcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('title_CN', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('title_EN', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('discription_CN', self.gf('django.db.models.fields.TextField')(max_length=10000, null=True, blank=True)),
            ('discription_EN', self.gf('django.db.models.fields.TextField')(max_length=10000, null=True, blank=True)),
        ))
        db.send_create_signal('Discussion', ['ThreadCategory'])

        # Adding model 'ThreadContent'
        db.create_table('Discussion_threadcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('Content', self.gf('django.db.models.fields.TextField')(max_length=10000, null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['KFLProduct.Language'], null=True, blank=True)),
            ('posted_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['KFLProduct.UserProfile'], null=True, blank=True)),
            ('posted_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('replied_by_master', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('Discussion', ['ThreadContent'])

        # Adding M2M table for field related_thread on 'ThreadContent'
        m2m_table_name = db.shorten_name('Discussion_threadcontent_related_thread')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_threadcontent', models.ForeignKey(orm['Discussion.threadcontent'], null=False)),
            ('to_threadcontent', models.ForeignKey(orm['Discussion.threadcontent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_threadcontent_id', 'to_threadcontent_id'])

        # Deleting field 'Thread.in_language'
        db.delete_column('Discussion_thread', 'in_language_id')

        # Deleting field 'Thread.posted_by'
        db.delete_column('Discussion_thread', 'posted_by_id')

        # Deleting field 'Thread.replied_by_master'
        db.delete_column('Discussion_thread', 'replied_by_master')

        # Deleting field 'Thread.topic'
        db.delete_column('Discussion_thread', 'topic')

        # Deleting field 'Thread.posted_on'
        db.delete_column('Discussion_thread', 'posted_on')

        # Deleting field 'Thread.Content'
        db.delete_column('Discussion_thread', 'Content')

        # Adding field 'Thread.pid'
        db.add_column('Discussion_thread', 'pid',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Thread.category'
        db.add_column('Discussion_thread', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['Discussion.ThreadCategory'], blank=True),
                      keep_default=False)

        # Adding field 'Thread.youtube_link'
        db.add_column('Discussion_thread', 'youtube_link',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Thread.youku_link'
        db.add_column('Discussion_thread', 'youku_link',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field translated_thread on 'Thread'
        db.delete_table(db.shorten_name('Discussion_thread_translated_thread'))

        # Removing M2M table for field related_thread on 'Thread'
        db.delete_table(db.shorten_name('Discussion_thread_related_thread'))


    def backwards(self, orm):
        # Deleting model 'ThreadCategory'
        db.delete_table('Discussion_threadcategory')

        # Deleting model 'ThreadContent'
        db.delete_table('Discussion_threadcontent')

        # Removing M2M table for field related_thread on 'ThreadContent'
        db.delete_table(db.shorten_name('Discussion_threadcontent_related_thread'))

        # Adding field 'Thread.in_language'
        db.add_column('Discussion_thread', 'in_language',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['KFLProduct.Language'], blank=True),
                      keep_default=False)

        # Adding field 'Thread.posted_by'
        db.add_column('Discussion_thread', 'posted_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['KFLProduct.UserProfile'], blank=True),
                      keep_default=False)

        # Adding field 'Thread.replied_by_master'
        db.add_column('Discussion_thread', 'replied_by_master',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Thread.topic'
        db.add_column('Discussion_thread', 'topic',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=400),
                      keep_default=False)

        # Adding field 'Thread.posted_on'
        db.add_column('Discussion_thread', 'posted_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Thread.Content'
        db.add_column('Discussion_thread', 'Content',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True, max_length=10000),
                      keep_default=False)

        # Deleting field 'Thread.pid'
        db.delete_column('Discussion_thread', 'pid')

        # Deleting field 'Thread.category'
        db.delete_column('Discussion_thread', 'category_id')

        # Deleting field 'Thread.youtube_link'
        db.delete_column('Discussion_thread', 'youtube_link')

        # Deleting field 'Thread.youku_link'
        db.delete_column('Discussion_thread', 'youku_link')

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


    models = {
        'Discussion.reply': {
            'Content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Reply'},
            'following_reply': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Discussion.Reply']", 'null': 'True', 'blank': 'True'}),
            'following_thread': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Discussion.Thread']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.UserProfile']", 'null': 'True', 'blank': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'Discussion.thread': {
            'Meta': {'object_name': 'Thread'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Discussion.ThreadCategory']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'Discussion.threadcategory': {
            'Meta': {'object_name': 'ThreadCategory'},
            'discription_CN': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'Discussion.threadcontent': {
            'Content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'ThreadContent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']", 'null': 'True', 'blank': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.UserProfile']", 'null': 'True', 'blank': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'related_thread': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_thread_rel_+'", 'to': "orm['Discussion.ThreadContent']", 'null': 'True', 'blank': 'True'}),
            'replied_by_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.ProductCategory']", 'null': 'True', 'blank': 'True'}),
            'discription_CN': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['KFLProduct.Language']", 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['KFLProduct.downloadProduct']", 'null': 'True', 'blank': 'True'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'paypal_button_on_sale': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'price_on_sale': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'customer_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']"}),
            'last_viewed_product': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'v_product'", 'symmetrical': 'False', 'to': "orm['KFLProduct.DVDProduct']", 'null': 'True', 'blank': 'True'}),
            'purchased_product': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'p_product'", 'symmetrical': 'False', 'to': "orm['KFLProduct.DVDProduct']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
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
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Discussion']