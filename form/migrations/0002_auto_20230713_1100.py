from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),  # Replace with the actual migration file
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE form_alist "
            "MODIFY COLUMN c_f TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, "
            "MODIFY COLUMN k_f TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, "
            "MODIFY COLUMN h_f TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, "
            "MODIFY COLUMN n_f TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, "
            "MODIFY COLUMN g_f TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, "
            "MODIFY COLUMN i_f TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, "
            "MODIFY COLUMN s_f TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
            reverse_sql="",
        ),
    ]
