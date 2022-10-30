#!/bin/bash

#Loading fixtures data
# echo "Loading fixtures data"
# cat <<EOF | python manage.py loaddata fixtures/init.json
# EOF

sed -i 's/force_text/force_str/' /usr/local/lib/python3.9/site-packages/graphene_django/utils/utils.py


python manage.py makemigrations
python manage.py migrate


echo "Creating super user admin if it does not exist"
cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()  # get the currently active user model,

User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', '', 'admin')
EOF

echo "Loading fixtures data"
cat <<EOF | python manage.py loaddata task/fixtures/init.json
EOF


# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000