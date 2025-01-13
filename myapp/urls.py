from django.urls import path
from . import views
urlpatterns = [
   path('',views.index, name='index'),
   path('user',views.user, name='user'),
   path('signin',views.signin, name='signin'),
   path('signup',views.signup, name='signup'),
   path('install',views.install,name='install'),
   path('transactions',views.transactions,name='transactions'),
   path('backup',views.backupt,name='backup'),
   path('backuph',views.backuph,name='backuph'),
   path('withdraw',views.withdraw,name='withdraw'),
   path('whistory',views.whistory,name='whistory'),
   path('bckwh',views.bckwh,name='bckwh'),
   path('bh',views.bh,name='bh'),
   path('lw',views.lw,name='lw'),
   path('con_w/<str:id>',views.conw,name='con_w'),
   path('card',views.card,name='card'),
   path('myprofile',views.myprofile,name='myprofile'),
   path('profup/<str:id>',views.profup,name='profup'),
   path('buyc',views.buyc,name='buyc'),
   path('logout',views.logout,name='logout'),
   path('generate_ref_link',views.generate_ref_link,name='generate_ref_link'),
   path('fundsr',views.fundsr,name='fundsr'),
   path('cardpayment',views.cardpayment,name='cardpayment'),
   path('cardspayment/<str:id>',views.cardspayment,name='cardspayment'),
   path('mycards',views.mycards,name='mycards'),
   path('humindex',views.humindex,name='humindex'),
   path('charitypay/<str:id>',views.charitypay,name='charitypay'),
   path('chargiftc',views.chargiftc,name='chargiftc'),
   path('mydano',views.mydano,name='mydano'),
   path('medbed',views.medbedhome,name='medbed'),
   path('cartapply',views.cartapply,name='cartapply'),
   path('veri_page',views.veri_page,name='veri_page'),
   path('home',views.home,name='home'),
   path('a',views.a,name='a'),
   path('trbp',views.trbp,name='trbp'),
]
# admin012


# bkdb
# pass = 9387$##THus75


# admin@mail.com
# myPASS1122