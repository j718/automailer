# An Automated Email Sender

``` bash
pip install automailer
```

## Usage

### file structure
Create the following file structure.

```
/
    /data
       email_list.csv
       message.md 
```

### message.md

``` markdown

---
subject: Required Subject for Email
sender: Required Gmail sender
password: OTP for gmail sender
---

Hi {name},

The cool thing about this file is that you can add any column included in your csv and it will populate. 
Your favorite color is {favorite_color}.

Best,

Sender
```

### email_list.csv
The only required column for this file is `email`.

``` csv
name, favorite_color, email
Jacob, Green, jacob@gmail.com
```

### Run

Change to root of project. 

``` bash
python -m automailer
```