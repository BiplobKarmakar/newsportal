# News Portal (CRUD + Auth)

A simple Django web application that allows users to view, create, edit, and delete news articles with media support and authentication.

---

## 📌 Features

- **User Authentication**: User registration, login, and logout using Django's built-in `User` model.
- **News Article CRUD Operations**:
  - **Create**: Authenticated users can publish new articles with titles, content, and thumbnails.
  - **Read**: Anyone (including guest visitors) can view published news articles and detail views.
  - **Update**: Edit existing news articles.
  - **Delete**: Delete news articles with a confirmation step.
- **Media Support**: Image thumbnail uploads for each article using `Pillow`.
- **Admin Panel**: Full access to manage users, news articles, and permissions.
- **UI/UX**: Responsive styling integrated with **Bootstrap 5**.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.14 / Django 6.1
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Version Control**: Git & GitHub

---

## 📋 News Model Structure

| Field | Type | Description |
| :--- | :--- | :--- |
| `title` | `CharField` | Article title |
| `content` | `TextField` | Full text content of the article |
| `thumbnail` | `ImageField` | Optional thumbnail image |
| `published_date` | `DateTimeField` | Automatically set on creation |
| `author` | `ForeignKey` | Link to Django's built-in `User` model |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/BiplobKarmakar/newsportal.git](https://github.com/BiplobKarmakar/newsportal.git)
cd newsportal 

python -m venv myenv
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate 

pip install -r requirements.txt 

python manage.py migrate 

python manage.py createsuperuser 

python manage.py runserver