from django.db import models

class alist(models.Model):
    id = models.AutoField(primary_key=True)
    a_f = models.TextField(blank=True, null=True)
    b_f = models.TextField(blank=True, null=True)
    c_f = models.TextField(blank=True, null=True)
    d_f = models.TextField(blank=True, null=True)
    e_f = models.TextField(blank=True, null=True)
    f_f = models.TextField(blank=True, null=True)
    g_f = models.TextField(blank=True, null=True)
    h_f = models.TextField(blank=True, null=True)
    i_f = models.TextField(blank=True, null=True)
    j_f = models.TextField(blank=True, null=True)
    k_f = models.TextField(blank=True, null=True)
    l_f = models.TextField(blank=True, null=True)
    m_f = models.TextField(blank=True, null=True)
    n_f = models.TextField(blank=True, null=True)
    o_f = models.TextField(blank=True, null=True)
    p_f = models.TextField(blank=True, null=True)
    q_f = models.TextField(blank=True, null=True)
    r_f = models.TextField(blank=True, null=True)
    s_f = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True, verbose_name='更新時間')
    class Meta:
        app_label = 'form'  
        db_table = 'form_alist'
    def __str__(self):
        return f"alist(id={self.id})"

class blist(models.Model):
    id = models.AutoField(primary_key=True)
    a_f = models.TextField(blank=True, null=True)
    b_f = models.TextField(blank=True, null=True)
    c_f = models.TextField(blank=True, null=True)
    d_f = models.TextField(blank=True, null=True)
    e_f = models.TextField(blank=True, null=True)
    f_f = models.TextField(blank=True, null=True)
    g_f = models.TextField(blank=True, null=True)
    h_f = models.TextField(blank=True, null=True)
    i_f = models.TextField(blank=True, null=True)
    j_f = models.TextField(blank=True, null=True)
    k_f = models.TextField(blank=True, null=True)
    l_f = models.TextField(blank=True, null=True)
    m_f = models.TextField(blank=True, null=True)
    n_f = models.TextField(blank=True, null=True)
    o_f = models.TextField(blank=True, null=True)
    p_f = models.TextField(blank=True, null=True)
    q_f = models.TextField(blank=True, null=True)
    r_f = models.TextField(blank=True, null=True)
    s_f = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True, verbose_name='更新時間')

    class Meta:
        app_label = 'form'  
        db_table = 'form_blist'

    def __str__(self):
        return f"blsit(id={self.id})"


class fields(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='原名稱')
    new_name = models.TextField(blank=True, null=True, verbose_name='欄位名稱')
    hide = models.CharField(max_length=5, blank=True, null=True, verbose_name='隱藏欄位')
    width = models.IntegerField(default=12, verbose_name='寬度')
    create_date = models.DateTimeField(verbose_name='建立日期')
    
    class Meta:
        db_table = 'form_fields' 
