![imgage](https://github.com/yunsonbai/yunorm/blob/master/yunorm.jpg)

Yunorm is a small ORM. 

* a small ORM but It's very practical
* python3.5 and 3.6 (developed with 3.5)
* support mysql, support mysql connections pool
* can help you to maintenance the DB connection
* support to create multiple database connections

## Requirements
* mysqlclient==1.3.14

## Install
* git clone git@github.com:yunsonbai/yunorm.git
* python setup.py install

## Quick Start
 [example](https://github.com/yunsonbai/yunorm/tree/master/example)

## note
If you want to use yunorm, the table that you will operate on must be exist in DB.


## Documentation
* field
  * Prikey
  * CharField
  * IntegerField
  * DateTimeField
  * DecimalField

* filter operator
  * lt: '<'
  * gt: '>'
  * une: '!='
  * lte: '<='
  * gte: '>='
  * in: 'in'

* function
  * filter
  * create
  * update
  * delete 
  * limit
  * order_by
  * group_by
  * desc_order_by
  * first
  * all
  * count
* note
if you want to get db data, you need call data() in the end
```python
  res = TestModel.objects.filter(**select_term).all().data()
  res = TestModel.objects.filter(**select_term).limit(0, 10).data()
  res = TestModel.objects.filter(
    **select_term).order_by(id).limit(0, 7).data()
```

* Get Data
```
  select_term = {
    "zan_num__gt": 0,
    "id__gt": 3700000
  }
  res = TestModel.objects.filter(**select_term).all().data()
  feed = TestModel.objects.filter(id=3700000).first().data()
```
* Create Data
```python
  def test_create_orm(i):
    create_data = {
      'label': 1,
      'title': 'test_{0}'.format(i)
    }
    TestOrm.create(**create_data)
```

* Update Data
```python
  def test_update_orm():
    update_data = {
      'title': 'hello yunsonbai',
      'label': 10
    }
    res = TestOrm.objects.filter(id__in=[1, 2]).data()
    for r in res:
      r.update(**update_data)
    # or
    res = TestOrm.objects.filter(id=3).first().data()
    res.update(**update_data)
```
* Delete Data
```python
  def test_delete_orm():
    res = TestOrm.objects.filter(id__in=[7, ]).data()
    for r in res:
      result = r.delete()
      print(result)
```
