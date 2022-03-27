# EventTracker
Track concerned envent key word by google search console and sent notification by email.

## Conda Dev Env
```
conda create --name et python=3.8 -y
```

## Template of file: `settings.ini`
```
[MailSender]
Name = Sender Name
Mail = sender@gmail.com
Password = sender_gmail_pwd

[Log]
Mail = logger@gmail.com
```

## test client data
```json
{
  "mail": "edwardxxx@gmail.com",
  "event": "111年 上半年 替代役"
}
```

```json
{
  "mail": "edwardxxx@gmail.com",
  "event": "郭雪芙 華燈初上"
}
```

```json
{
  "mail": "howardxxx@gmail.com",
  "event": "111年 上半年 替代役"
}
```