# Social Media API Project

This project is a straightforward social media API developed using **Django** and **Django REST Framework**. It features custom user authentication and token-based authentication for API requests.

## Table of Contents

- Project Setup
- User Model Overview
- Registering a User
- Authenticating a User
- Testing the API
- Implementing Posts and Comments Functionality
- Implementing User Follows and Feed Functionality

## Project Setup

To set up the project locally, follow these steps:

- **Clone the Repository**
  ```bash
  git clone https://github.com/<your-username>/social_media_api.git
  cd <your-repository>
  ```

- **Create a Virtual Environment**
  Set up a virtual environment to isolate project dependencies.
  ```bash
  python -m venv .env
  source .env/bin/activate  # On MacOS 
  .env\Scripts\activate      # On Windows
  ```

- **Install Dependencies**
  ```bash
  pip install -r requirements.txt
  ```

- **Set Up the Database**
  Apply migrations to configure the database schema.
  ```bash
  python manage.py migrate
  ```

- **Run the Development Server**
  Start the Django development server.
  ```bash
  python manage.py runserver
  ```
  Your local development server will be accessible at: `http://127.0.0.1:8000/`.

## User Model Overview

The custom user model extends Django's `AbstractUser` and includes the following additional fields:

- **bio:** A text field for users to add a brief biography.
- **profile_picture:** An image field for users to upload a profile picture.
- **followers:** A Many-to-Many field to track user followers, referencing the User model itself (with `symmetrical=False` to allow one-way following).

### User Model Example

```python
# social_media_api/accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
  
    def __str__(self):
        return self.username
```

## Registering a User

To register a user, send a POST request to the `http://127.0.0.1:8000/api/accounts/register/` endpoint.

- **Register Endpoint:** 
  - **POST** `http://127.0.0.1:8000/api/accounts/register/`

### Request Body (JSON):

```json
{
  "username": "kssibuta",
  "password": "byg6zmA2ss.",
  "bio": "kssibuta's bio"
}
```

```json
{
  "username": "sibuta",
  "password": "qyg6zmW3ss.",
  "bio": "sibuta's bio"
}
```

### Response (Success):

```json
{
  "status": "User created successfully",
  "token": "86eb3d31a8579246b218e8b212fb2c1c18f91921",
  "user": {
      "username": "kssibuta",
      "bio": "kssibuta's bio"
  }
}
```

The response will include a token for authentication in future API requests.

## Authenticating a User

This API employs token-based authentication. After registration, users receive a token that should be included in the header of every request requiring authentication.

- **Login Endpoint:** 
  - **POST** `http://127.0.0.1:8000/api/accounts/login/`

### Request Body (JSON):

```json
{
  "username": "kssibuta",
  "password": "byg6zmA2ss."
}
```

```json
{
  "username": "sibuta",
  "password": "qyg6zmW3ss."
}
```

### Response (Success):

```json
{
  "token": "86eb3d31a8579246b218e8b212fb2c1c18f91921"
}
```

### Using the Token

For authenticated requests, include the token in the Authorization header as a Bearer token.

```
Authorization: Token generated_token_here
```

## Testing the API

To test the registration and authentication flows, you can use tools like **Postman** or **Curl**.

### Registration with Curl Example:

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
-H "Content-Type: application/json" \
-d '{"username": "kssibuta", "password": "byg6zmA2ss..", "bio": "sibuta's bio"}'
```

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
-H "Content-Type: application/json" \
-d '{"username": "sibuta", "password": "byg6zmW3ss.", "bio": "sibuta's bio"}'
```

### Login with Curl Example:

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
-H "Content-Type: application/json" \
-d '{"username": "kssibuta", "password": "byg6zmA2ss."}'
```

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
-H "Content-Type: application/json" \
-d '{"username": "", "password": ""}'
```

Make sure to replace `username` and `password` with actual user credentials during testing.

## Implementing Posts and Comments Functionality

### Overview

Users can manage posts and interact through comments within the social media platform by creating, viewing, updating, and deleting posts and comments. The API provides endpoints for these operations, with user authentication and permissions.

### Endpoints

#### Posts API

- **Authentication:** Required for creating, updating, and deleting posts and comments. Create a user account using the Django Admin portal or run `python manage.py drf_create_token <username>` to generate a token for access.
  
- **Permissions:** Only the author of a post or comment can update or delete it. Anyone can view posts and comments.

- **Testing:** All endpoints have been thoroughly tested using Postman, with examples provided in this documentation to demonstrate functionality.

### Create a New Post

- **URL:** `http://127.0.0.1:8000/api/posts/`
- **Method:** POST
- **Authentication Required:** Yes
- **Description:** Allows authenticated users to create a new post.

#### Request Body:

```json
{
    "title": "First Post",
    "content": "What a journey to this point."
}
```

#### Response:

```json
{
    "id": 1,
    "author": "Festus",
    "title": "First Post",
    "content": "You're making a good progress.",
    "created_at": "2024-09-20T12:05:05.430148Z",
    "updated_at": "2024-09-20T12:05:05.430148Z"
}
```

### Retrieve a List of Posts

- **URL:** `http://127.0.0.1:8000/api/posts/`
- **Method:** GET
- **Authentication Required:** No
- **Description:** Retrieve a list of all posts with pagination.

#### Response:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "kssibuta",
            "title": "First Post",
            "content": "What a journey to this point.",
            "created_at": "2024-09-20T12:05:05.430148Z",
            "updated_at": "2024-09-20T12:05:05.430148Z"
        }
    ]
}
```

### Retrieve a Single Post

- **URL:** `http://127.0.0.1:8000/api/posts/1/`
- **Method:** GET
- **Authentication Required:** No
- **Description:** Retrieve a specific post by its ID.

#### Response:

```json
{
    "id": 1,
    "author": "kssibuta",
    "title": "First Post",
    "content": "What a journey to this point.",
    "created_at": "2024-09-20T12:05:05.430148Z",
    "updated_at": "2024-09-20T12:05:05.430148Z"
}
```

### Update a Post

- **URL:** `http://127.0.0.1:8000/api/posts/1/`
- **Method:** PUT
- **Authentication Required:** Yes
- **Description:** Allows the post's author to update the post.

#### Request Body:

```json
{
    "title": "First Post Updated",
    "content": "You are making a good progress."
}
```

#### Response:

```json
{
    "id": 1,
    "author": "kssibuta",
    "title": "First Post Updated",
    "content": "coding master.",
    "created_at": "2024-09-20T12:05:05.430148Z",
    "updated_at": "2024-09-20T12:14:45.893056Z"
}
```

### Delete a Post

- **URL:** `http://127.0.0.1:8000/api/posts/1/`
- **Method:** DELETE
- **Authentication Required:** Yes
- **Description:** Allows the post's author to delete the post.

#### Response:

```json
{
    "detail": "Post deleted successfully."
}
```

### Comments API

#### Create a New Comment

- **URL:** `http://127.0.0.1:8000/api/comments/`
- **Method:** POST
- **Authentication Required:** Yes
- **Description:** Allows authenticated users to add a comment to a post.

#### Request Body:

```json
{
    "post": 1,
    "content": "Congrats on making it this far."
}
```

#### Response:

```json
{
    "id": 2,
    "post": 1,
    "author": "sibuta",
    "content": "Congrats on making it this far.",
    "created_at": "2024-09-20T13:36:48.304820Z",
    "updated_at": "2024-09-20T13:36:48.304820Z"
}
```

#### Retrieve a List of Comments

- **URL:** `http://127.0.0.1:8000/api/comments/`
- **Method:** GET
- **Authentication Required:** No
- **Description:** Retrieve a list of all comments with pagination.

#### Response:

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "post": 1,
            "author": "sibuta",
            "content": "Congrats on making it this far.",
            "created_at": "2024-09-20T12:17:08.356204Z",
            "updated_at": "2024-09-20T12:17:08.356204Z"
        },
        {
            "id": 2,
            "post": 1,
            "author": "sibuta",
            "content": "Congrats on making it this far.",
            "created_at": "2024-09-20T13:36:48.304820Z",
            "updated_at": "2024-09-20T13:36:48.304820Z"
        }
    ]
}
```

#### Update a Comment

- **URL:** `http://127.0.0.1:8000/api/comments/1/`
- **Method:** PUT
- **Authentication Required:** Yes
- **Description:** Allows the comment's author to update the comment.

#### Request Body:

```json
{
    "post": 1,
    "content": "Slow but sure progress."
}
```

#### Response:

```json
{
    "id": 1,
    "post": 1,
    "author": "sibuta",
    "content": "Slow but sure progress.",
    "created_at": "2024-09-20T12:17:08.356204Z",
    "updated_at": "2024-09-20T13:45:17.194217Z"
}
```

#### Delete a Comment

- **URL:** `http://127.0.0.1:8000/api/comments/1/`
- **Method:** DELETE
- **Authentication Required:** Yes
- **Description:** Allows the comment's author to delete the comment.

#### Response:

```json
{
    "detail": "Comment deleted successfully."
}
```

### Filtering and Searching

- **Filtering Posts:** You can filter posts by title using the query parameter `title`.
  - **Example Request:**
    ```
    GET /api/posts/?title=First%20Post
    ```

- **Searching Posts:** You can search posts by title or content using the `search` query parameter.
  - **Example Request:**
    ```
    GET /api/posts/?search=content
    ```

- **Pagination:** All list endpoints support pagination, with a default page size of 5.
  - **Example Request:**
    ```
    GET /api/posts/?page=2
    ```

## Implementing User Follows and Feed Functionality

### User Follow API

- **Follow User**
  - **URL:** `http://127.0.0.1:8000/api/accounts/follow/1/`
  - **Method:** POST
  - **Authentication Required:** Yes
  - **Description:** Allows authenticated users to follow another user.

#### Response:

```json
{
    "message": "User followed successfully"
}
```

- **Unfollow User**
  - **URL:** `http://127.0.0.1:8000/api/accounts/unfollow/1/`
  - **Method:** POST
  - **Authentication Required:** Yes
  - **Description:** Allows authenticated users to unfollow another user.

#### Response:

```json
{
    "message": "User unfollowed successfully"
}
```

### Feed API

- **Get User Feed**
  - **URL:** `http://127.0.0.1:8000/api/feed`
  - **Method:** GET
  - **Authentication Required:** Yes
  - **Description:** Returns posts from followed users, ordered by creation date (most recent first) and supports pagination.

#### Response:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "kssibuta",
            "title": "First Post Updated",
            "content": "What a journey to this point and beyond.",
            "created_at": "2024-09-20T12:05:05.430148Z",
            "updated_at": "2024-09-20T12:14:45.893056Z",
            "comments": [
                {
                    "id": 1,
                    "post": 1,
                    "author": "sibuta",
                    "content": "Slow but sure progress.",
                    "created_at": "2024-09-20T12:17:08.356204Z",
                    "updated_at": "2024-09-20T13:45:17.194217Z"
                },
                {
                    "id": 2,
                    "post": 1,
                    "author": "sibuta",
                    "content": "Congratulations for making it this far.",
                    "created_at": "2024-09-20T13:36:48.304820Z",
                    "updated_at": "2024-09-20T13:36:48.304820Z"
                }
            ],
            "likes_count": 0
        }
    ]
}
```

### Likes API

- **Like a Post**
  - **URL:** `http://127.0.0.1:8000/api/posts/1/like/`
  - **Method:** POST
  - **Authentication Required:** Yes
  - **Description:** Allows users to like a post.

#### Response:

```json
{
    "status": "post liked"
}
```

- **Unlike a Post**
  - **URL:** `http://127.0.0.1:8000/api/posts/1/unlike/`
  - **Method:** POST
  - **Authentication Required:** Yes
  - **Description:** Allows users to unlike a post.

#### Response:

```json
{
    "status": "post unliked"
}
```

### Notifications API

- **Get User Notifications**
  - **URL:** `http://127.0.0.1:8000/api/notifications/`
  - **Method:** GET
  - **Authentication Required:** Yes
  - **Description:** Returns a list of notifications for the authenticated user, supporting pagination.

#### Response:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "actor": "kssibuta",
            "verb": "liked your post",
            "target": "First Post Updated",
            "timestamp": "2024-09-22T09:34:59.097560Z",
            "is_read": false
        }
    ]
}
```

- **Mark Notification as Read**
  - **URL:** `http://127.0.0.1:8000/api/notifications/1/mark-read/`
  - **Method:** POST
  - **Authentication Required:** Yes
  - **Description:** Marks the specified notification as read.

#### Response:

```json
{
    "detail": "Notification marked as read."
}
```

---

Feel free to adjust any sections as needed!