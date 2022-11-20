poetry build -f wheel
poetry run pip install --upgrade -t package dist/*.whl
cd package
zip -r ../artifact.zip . -x '*.pyc'
aws s3 cp ../artifact.zip s3://todo-escalator
