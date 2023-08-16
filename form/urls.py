from django.urls import path
from . import views
#my urls
urlpatterns = [
    path("getFields/",views.getFields,name="get_fields"),
    path("getDataList/",views.getDataList,name="get_List_Data"),
    path("updateDataList/",views.updateListData,name="update_List_Data"),
    path("addDataList/",views.addListData,name="add_List_Data"),
    path("deleteDataList/",views.deleteListData,name="delete_List_Data"),
    path("hideFields/",views.hideFields,name="hide_form_fields"),
    path("unhideFields/",views.unhideFields,name="unhide_form_fields"),
    path("setWidth/",views.update_fields,name="set_Width")
]

