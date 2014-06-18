from django.conf.urls import patterns, include, url
from django.contrib import admin
import os
# from django.contrib.auth.views import login, logout
# from AuthTool.views import *
# from KPISetter.views import *
# from BonuSimulation.views import *
# from ResultUpdater.views import *
# from LockManagement.views import *

import KFLProduct.views
import Tutorial.views
import Discussion.views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^MEDIA/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), "MEDIA"), 'show_indexes': True }),

    url(r'^admin/', include(admin.site.urls)),

    # from AuthTool----------------------------------------------------
    url(r'^accounts/login/$', KFLProduct.views.login),
    url(r'^accounts/logout/$', KFLProduct.views.logout),
    url(r'^accounts/personal_information/$', KFLProduct.views.personal_information),    
    url(r'^set_cn/$', KFLProduct.views.set_cn),
    url(r'^set_en/$', KFLProduct.views.set_en),

    # url(r'^secretreset/$', secretreset),

    url(r'^tutorials/overview/$', Tutorial.views.overview),
    url(r'^tutorials/(?P<tutorialname>[\w\-]+)/$', Tutorial.views.tutorialview, name="tutorialdisplay"),     

    url(r'^products/overview/$', KFLProduct.views.overview, name="productoverview"),
    url(r'^products/(?P<productname>[\w\-]+)/$', KFLProduct.views.productview, name="productdisplay"),     
    url(r'^products/category/(\d+)/$', KFLProduct.views.productcategory, name="productcategory"),     
    url(r'^products/bundle/(\d+)/$', KFLProduct.views.productbundleview, name="bundledisplay"),     

    url(r'^discussion/overview/$', Discussion.views.overview),
    url(r'^discussion/category/(\d+)/$', Discussion.views.threadcategory, name="threadcategory"),     
    url(r'^discussion/searchresults/$', Discussion.views.threadresult),     
    url(r'^discussion/searchresults/(?P<posted_by>[\w\-]+)/$', Discussion.views.threadresultpostedby, name="threadpostedby"),     
    url(r'^discussion/searchresults/inlanguage/(?P<inlanguage>[\w\-]+)/$', Discussion.views.threadresultinlanguage, name="threadinlanguage"),     

    url(r'^discussion/post/(\d+)/$', Discussion.views.threadpost, name="postcategory"),     
    url(r'^discussion/thread/(\d+)/$', Discussion.views.threaddetail, name="threaddetail"),     
    url(r'^discussion/topic/(\d+)/language/(\d+)/$', Discussion.views.topiclanguagesearch, name="topiclanguagesearch"),     

    url(r'^discussion/thread/(\d+)/(\d+)/reply/$', Discussion.views.postreply, name="postreply"),     
    url(r'^discussion/post/reply/(\d+)/(\d+)/$', Discussion.views.replyreply, name="replyreply"),     
    url(r'^discussion/topic/(\d+)/thread/(\d+)/translate/$', Discussion.views.threadtranslate, name="threadtranslate"),     
    url(r'^discussion/topic/(\d+)/delete/$', Discussion.views.threaddelete, name="threaddelete"),     

    url(r'^discussion/thread/(\d+)/masterreply/$', Discussion.views.masterreply, name="masterreply"),     


    # # from KPISetter----------------------------------------------------
    


    # url(r'^accounts/personal_information/$', personal_information),
    # url(r'^personal_data/$', personal_data_overview),
    # url(r'^personal_KPI/$', personal_KPI_overview),
    # url(r'^forecast_data/$', forecast_data_overview),
    # # url(r'^allsales_data/$', allsales_data),

    # # from personal_data
    # url(r'^personal_data/(?P<unitname>[\w\-]+)/(?P<membername>[\w\-]+)/$', personal_data, name="pdatadisplay"),     
    # url(r'^personal_data/(?P<unitname>[\w\-]+)/(?P<membername>[\w\-]+)/newyear$', npersonal_data, name="npdatadisplay"),   
    # url(r'^personal_archive/(\d+)/$', personal_archive, name="pdatadownload"),   
    # url(r'^personal_archive_overview/$', personal_archive_overview),   

    
    # url(r'^personal_KPI/(?P<unitname>[\w\-]+)/(?P<membername>[\w\-]+)/$', KPI_data, name="pkidatadisplay"),     
    # url(r'^personal_KPI/(?P<unitname>[\w\-]+)/(?P<membername>[\w\-]+)/newyear$', nKPI_data, name="npkidatadisplay"),     
    
    # url(r'^group_data/(?P<unitname>[\w\-]+)/$', unit_data, name="gdatadisplay"),
    # url(r'^forecast_data/(?P<unitname>[\w\-]+)/(?P<membername>[\w\-]+)/$', forecast_data, name="foredatadisplay"),     
    # url(r'^forecast_data/(?P<unitname>[\w\-]+)/(?P<membername>[\w\-]+)/newyear$', nforecast_data, name="nforedatadisplay"),     
    # # HR ATI Editer


    # # Overall Structure Definition
    # url(r'^overall_structure/$', overall_structure),


    # # from BonuSimulation----------------------------------------------------
    # url(r'^personal_info_updatepage/$', personal_info_updatepage),
    # url(r'^personal_info_template_download/$', personal_info_template_download),
    # url(r'^simulation_data/$', simulation_data),




    # # from result updater-------------------------
    # url(r'^result_updatepage/$', result_updatepage),
    # url(r'^result_template_download/$', result_template_download),


    # # from Lock Management-------------------------
    # # url(r'^verify_data/(\d+)/$', verify_data),
    # url(r'^lock_data/(\d+)/$', lock_data),
    # url(r'^lock_data/$', lock_data_overview),
    # # url(r'^modification_request/$', modification_request),


    # # url(r'^download_result/(?P<filename>[\w\-]+)/$', download_result, name='downresults'),
    # url(r'^download_result/(?P<filename>[\w\-]+)/(?P<quarter>\d+)/$', download_result, name="downresults"),
    # url(r'^download_result_overview/$', download_result_overview),
    # url(r'^make_result_HR/(\d+)/$', make_result_HR, name="make_HR_result"),    


    # url(r'^HR_download_result/(?P<filename>[\w\-]+)/$', HR_download_result, name="HRdownresults"),
    # url(r'^HR_download_result_overview/$', HR_download_result_overview),


    # # url(r'^temp/$', ArchiveAll_temp),

    # # url(r'^request_confirm/(\d+)/$', request_confirm, name="r_cfm"),
    # # url(r'^request_reject/(\d+)/$', request_reject, name="r_rej"),
    # # url(r'^request_acknowledge/(\d+)/$', request_acknowledge, name="r_ack"),


    # # url(r'^jfaoweifj/$', jfaoweifj),

    url(r'^.*/$', KFLProduct.views.homepage),

)
