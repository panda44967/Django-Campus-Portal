# campus_vote — Django Shell 操作記錄

學號：P1146106  
Django 版本：5.0.0

---

## 一、建立虛擬環境與安裝 Django

```bash
# 在根目錄 exam1_P1146106/ 下建立虛擬環境
python -m venv .P1146106
source .P1146106/bin/activate          # Linux / macOS
# .P1146106\Scripts\activate           # Windows

pip install django==5.0.0
```

---

## 二、資料庫初始化指令

```bash
cd campus_vote

# 產生 migration 檔
python manage.py makemigrations polls

# 檢視初始 migration 對應的 SQL
python manage.py sqlmigrate polls 0001

# 套用 migration
python manage.py migrate
```

### sqlmigrate polls 0001 輸出（節錄）

```sql
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(200) NOT NULL,
    "pub_date" datetime NOT NULL,
    "description" text NOT NULL,
    "is_open" bool NOT NULL
);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL,
    "question_id" bigint NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED
);
COMMIT;
```

---

## 三、建立 Superuser

```bash
python manage.py createsuperuser
# Username: ntub
# Email: ntub@ntub.edu.tw
# Password: 123
```

---

## 四、Django Shell 操作

```bash
python manage.py shell
```

### 1. 查詢所有 Question

```python
>>> from polls.models import Question, Choice
>>> Question.objects.all()
<QuerySet [<Question: 是否需要增設飲水機？>,
           <Question: 校園講座是否改為雙語進行？>,
           <Question: 下學期社團博覽會要延長幾時上線？>]>
```

### 2. 取出第一筆 Question

```python
>>> q = Question.objects.first()
>>> q
<Question: 是否需要增設飲水機？>
>>> q.title
'是否需要增設飲水機？'
>>> q.is_open
False
>>> q.pub_date
datetime.datetime(2026, 4, 5, 8, 12, 0, tzinfo=datetime.timezone.utc)
```

### 3. 印出第一筆 Question 的所有 Choice

```python
>>> q.choice_set.all()
<QuerySet [<Choice: 是，目前嚴重不足>,
           <Choice: 否，已有足夠>,
           <Choice: 可增設部分樓層>]>
```

### 4. 把其中一個 Choice.votes 加 1 後儲存

```python
>>> c = q.choice_set.get(choice_text='是，目前嚴重不足')
>>> c.votes
12
>>> c.votes += 1
>>> c.save()
>>> # 重新查詢確認已儲存
>>> Choice.objects.get(pk=c.pk).votes
13
```

---

## 五、確認 superuser 存在

```python
>>> from django.contrib.auth.models import User
>>> User.objects.filter(is_superuser=True)
<QuerySet [<User: ntub>]>
```

---

## 六、啟動伺服器

```bash
python manage.py runserver
# 瀏覽 http://127.0.0.1:8000/
# Admin: http://127.0.0.1:8000/admin/
```
