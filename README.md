# tgpm — Telegram Project Manager

🌐 **Website / وبسایت:** [jahaniwww.com](https://jahaniwww.com) · 📣 **Telegram channel / کانال تلگرام:** [@tarfandoonchannel](https://t.me/tarfandoonchannel)

[English](#english) · [فارسی](#فارسی)

---

## English

**tgpm** keeps a project's roadmap, weekly plan and announcements inside a Telegram group, so a developer and a
project manager (or a client) can follow progress in one place without opening any other tool.

You write the roadmap as a normal Markdown checklist in your repository. After every change you run one command and
the Telegram messages update themselves:

- **Roadmap topic**: one message per week with a progress bar and ✅/⬜ for each task. It is edited in place and pinned.
- **Next-week plan topic**: the goals of the coming week and what is still open from the last one. Only the newest plan stays pinned.
- **Auto-advance**: when every task of the current week is ticked, the next week's roadmap and the plan after it are posted and pinned automatically.
- **Updates topic**: explicit announcements and files (`tgpm post`), only when you send them.
- Messages in **English or Persian**, with Gregorian, Jalali (Persian) or both dates.

No dependencies: the Python code uses only the standard library, and there is a ready single-file `tgpm.exe` for Windows.

### 1. Set up Telegram (once, ~5 minutes)

1. In Telegram open **@BotFather** → `/newbot` → copy the **token**.
2. Create a group (or use an existing one) and add the bot.
3. For one topic per section, turn on **Topics** in the group settings (the group becomes a "forum"). Without topics tgpm still works and posts into the main chat.
4. Make the bot an **admin** with the rights **Pin messages** and (if topics are on) **Manage topics**.
5. Find the group id: it looks like `-1001234567890` (forward a group message to **@RawDataBot**, or use any "get chat id" bot).

> **Keep the token secret.** It lives only in `.env`, which `tgpm init` adds to `.gitignore`. tgpm never prints it, logs it or writes it into messages. If it leaks, run `/revoke` in @BotFather.

### 2. Use it

```powershell
# in your project folder (use tgpm.exe, or: python -m tgpm ...)
tgpm init --name "My App" --lang en --calendar gregorian   # creates tgpm.json, .env, ROADMAP.md, .gitignore
# put TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID into .env, then:
tgpm check                 # verifies the token, the group, topics and the bot's rights
tgpm week 1 --dry-run      # preview the message (sends nothing)
tgpm week 1                # post (and pin) the roadmap of week 1
tgpm plan 2                # post (and pin) the plan of week 2
# ... work, tick tasks in ROADMAP.md ...
tgpm sync                  # edit every posted message; post the next week when this one is done
tgpm post --text "Release candidate is ready" --pin
tgpm post --document report.pdf --text "Weekly report"
tgpm status                # progress in the terminal, sends nothing
```

Tip: run `tgpm sync` after every change to `ROADMAP.md` (a git hook or CI step works well).

### 3. The roadmap file

```markdown
## Week 1: Foundation
- [x] Set up the repository and CI
- [ ] First working version of the core feature
- **Checkpoint 1: Friday**        (optional, shown in the plan)
- **Output:** a working core feature   (optional)

## Week 2: Launch
- [ ] ...
```

Headings `## Week N: ...` (also `Sprint`, `Phase`, `Milestone`, or Persian `## هفته N: ...`) start a week; `- [ ]` / `- [x]` lines are its tasks.

### 3b. Use it from AI coding agents (one command)

```powershell
tgpm agent install            # auto-detects Claude Code, Codex, Cline, Cursor, Gemini CLI
tgpm agent install all        # or name them: claude codex cline cursor gemini
tgpm agent install --global   # for your user instead of only this project
tgpm agent install --uninstall
```

It writes each tool's own format: Claude Code skill + `/tgpm-sync` command (and a `.claude-plugin` so the repo is installable as a plugin), a marked block in `AGENTS.md` (Codex) and `GEMINI.md`, `.clinerules/tgpm.md` (Cline), `.cursor/rules/tgpm.mdc` (Cursor). Re-running updates in place; your own text in shared files is kept. The agent is told never to read `.env`.

### 4. Commands

| Command | What it does |
|---|---|
| `tgpm init` | Creates `tgpm.json`, `.env` template, a sample `ROADMAP.md` and the `.gitignore` entries. Never overwrites without `--force`. |
| `tgpm check` | Checks token, group, topics and the bot's admin rights. |
| `tgpm week N [--dry-run]` | Posts or edits the roadmap message of week N (pinned on first post). |
| `tgpm plan N [--dry-run]` | Posts or edits the plan message of week N; older plans are unpinned. |
| `tgpm sync` | Edits all posted messages; advances to the next week when the current one is fully ticked. |
| `tgpm post` | Sends a **new** message/file to a topic (`--topic`, `--text`, `--file`, `--document`, `--pin`, `--raw-html`, `--dry-run`). |
| `tgpm status` | Prints progress from the roadmap file. |
| `tgpm agent install` | Installs tgpm instructions for AI coding agents (see 3b). |

Global option: `--dir <folder>` (default: current folder; `tgpm.json` is searched upwards).

### 5. Configuration (`tgpm.json`)

| Key | Meaning | Default |
|---|---|---|
| `project` | Name | folder name |
| `hashtag` | Hashtag added to messages (`""` = none) | name without spaces |
| `language` | `en` or `fa` | `en` |
| `calendar` | `gregorian`, `jalali` or `both` | `gregorian` |
| `roadmap_file` | Path to the Markdown roadmap | `ROADMAP.md` |
| `topics` | Topic names by key: `roadmap`, `plan`, `updates` (add your own keys for `tgpm post --topic`) | per language |
| `max_item_len` | Longest task text in a message | `120` |
| `advance` | Auto-post the next week when the current one is done | `true` |

State (message and topic ids) is kept in `.tgpm/state.json`. Delete a message in Telegram? Remove its id from that file and the next run posts a new one.

### 6. Build the executable yourself

```powershell
powershell -File build_exe.ps1     # runs the tests, then builds dist\tgpm.exe with PyInstaller
```

Run the tests alone: `python -m unittest discover -s tests -t .`

### Notes and limits

- tgpm only sends what you ask for: `week`, `plan`, `sync` and `post`. It never reads group messages.
- The token never appears in output or errors; network errors show only the error class.
- Telegram messages are limited to 4096 characters. Long weeks are shortened with "… and N more".
- Windows editors may add a BOM to `.env`/`tgpm.json`; tgpm reads both correctly.

License: MIT.

---

## فارسی

**tgpm** رودمپ، پلن هفتگی و اطلاعیه‌های یک پروژه را داخل یک گروه تلگرام نگه می‌دارد. به این ترتیب توسعه‌دهنده و مدیر پروژه (یا کارفرما) بدون باز کردن ابزار دیگری، پیشرفت کار را یک‌جا می‌بینند.

رودمپ را مثل یک چک‌لیست ساده‌ی Markdown در مخزن پروژه می‌نویسید. بعد از هر تغییر یک دستور می‌زنید و پیام‌های تلگرام خودشان به‌روز می‌شوند:

- **تاپیک رودمپ:** برای هر هفته یک پیام با نوار پیشرفت و ✅/⬜ برای هر کار. پیام همان‌جا ویرایش می‌شود (پیام جدید نمی‌آید) و پین است.
- **تاپیک پلن هفته آینده:** اهداف هفته‌ی بعد و کارهای مانده از هفته قبل. فقط جدیدترین پلن پین می‌ماند.
- **پیشروی خودکار:** وقتی همه‌ی کارهای هفته‌ی جاری تیک بخورد، رودمپ هفته‌ی بعد و پلن هفته‌ی بعدترش خودکار پست و پین می‌شود.
- **تاپیک به‌روزرسانی‌ها:** اطلاعیه و فایل (`tgpm post`)، فقط وقتی خودتان بفرستید.
- پیام‌ها **فارسی یا انگلیسی** هستند و تاریخ می‌تواند میلادی، شمسی یا هر دو باشد.

وابستگی ندارد: کد پایتون فقط از کتابخانه‌ی استاندارد استفاده می‌کند و برای ویندوز یک فایل اجرایی تک‌فایلی `tgpm.exe` هم هست.

### ۱. آماده‌سازی تلگرام (یک بار، حدود ۵ دقیقه)

۱. در تلگرام به **@BotFather** بروید ← `/newbot` ← **توکن** را کپی کنید.
۲. یک گروه بسازید (یا از گروه موجود استفاده کنید) و ربات را اضافه کنید.
۳. برای داشتن یک تاپیک به‌ازای هر بخش، در تنظیمات گروه **Topics** را روشن کنید (گروه «فروم» می‌شود). بدون تاپیک هم کار می‌کند و پیام‌ها در چت اصلی می‌روند.
۴. ربات را **ادمین** کنید با دسترسی **Pin messages** و (اگر تاپیک روشن است) **Manage topics**.
۵. شناسه‌ی گروه را پیدا کنید؛ شکلش `-1001234567890` است (یک پیام گروه را برای **@RawDataBot** فوروارد کنید یا از هر ربات «چت آیدی» استفاده کنید).

> **توکن را محرمانه نگه دارید.** فقط در `.env` می‌ماند و `tgpm init` آن را به `.gitignore` اضافه می‌کند. tgpm هرگز توکن را چاپ، لاگ یا داخل پیام نمی‌گذارد. اگر لو رفت، در @BotFather دستور `/revoke` را بزنید.

### ۲. استفاده

```powershell
# داخل پوشه‌ی پروژه (از tgpm.exe استفاده کنید، یا: python -m tgpm ...)
tgpm init --name "My App" --lang fa --calendar jalali   # tgpm.json، .env، ROADMAP.md و .gitignore را می‌سازد
# TELEGRAM_BOT_TOKEN و TELEGRAM_CHAT_ID را در .env بگذارید، بعد:
tgpm check                 # توکن، گروه، تاپیک‌ها و دسترسی‌های ربات را بررسی می‌کند
tgpm week 1 --dry-run      # پیش‌نمایش پیام (چیزی نمی‌فرستد)
tgpm week 1                # رودمپ هفته ۱ را پست و پین می‌کند
tgpm plan 2                # پلن هفته ۲ را پست و پین می‌کند
# ... کار کنید و در ROADMAP.md تیک بزنید ...
tgpm sync                  # همه‌ی پیام‌های پست‌شده را ویرایش می‌کند؛ اگر هفته کامل شد هفته‌ی بعد را پست می‌کند
tgpm post --text "نسخه‌ی آزمایشی آماده است" --pin
tgpm post --document report.pdf --text "گزارش هفتگی"
tgpm status                # پیشرفت را در ترمینال نشان می‌دهد، چیزی نمی‌فرستد
```

نکته: بعد از هر تغییر `ROADMAP.md` دستور `tgpm sync` را اجرا کنید (hook گیت یا یک مرحله‌ی CI هم مناسب است).

### ۳. فایل رودمپ

```markdown
## هفته ۱: پایه‌گذاری
- [x] راه‌اندازی مخزن و CI
- [ ] نسخه‌ی اول کارکرد اصلی
- **چک‌پوینت ۱: جمعه**          (اختیاری، در پلن نشان داده می‌شود)
- **خروجی:** کارکرد اصلی آماده     (اختیاری)

## هفته ۲: انتشار
- [ ] ...
```

عنوان `## هفته N: ...` (یا `Week` / `Sprint` / `Phase` / `Milestone` انگلیسی) یک هفته را شروع می‌کند و خط‌های `- [ ]` و `- [x]` کارهای آن هستند.

### ۳ب. استفاده از داخل ابزارهای هوش مصنوعی (با یک دستور)

```powershell
tgpm agent install            # Claude Code، Codex، Cline، Cursor و Gemini CLI را خودکار پیدا و نصب می‌کند
tgpm agent install all        # یا نام ببرید: claude codex cline cursor gemini
tgpm agent install --global   # برای کل کاربر، نه فقط همین پروژه
tgpm agent install --uninstall
```

برای هر ابزار فرمت خودش نوشته می‌شود: skill و دستور `/tgpm-sync` برای Claude Code (با `.claude-plugin` تا مخزن به‌شکل پلاگین هم نصب‌شدنی باشد)، یک بلوک علامت‌دار در `AGENTS.md` (Codex) و `GEMINI.md`، فایل `.clinerules/tgpm.md` (Cline) و `.cursor/rules/tgpm.mdc` (Cursor). اجرای دوباره فقط به‌روز می‌کند و متن خودتان در فایل‌های مشترک دست‌نخورده می‌ماند. به agent گفته شده هرگز `.env` را نخواند.

### ۴. دستورها

| دستور | کار |
|---|---|
| `tgpm init` | `tgpm.json`، الگوی `.env`، یک `ROADMAP.md` نمونه و ورودی‌های `.gitignore` را می‌سازد. بدون `--force` چیزی را بازنویسی نمی‌کند. |
| `tgpm check` | توکن، گروه، تاپیک‌ها و دسترسی ادمین ربات را بررسی می‌کند. |
| `tgpm week N [--dry-run]` | پیام رودمپ هفته‌ی N را پست یا ویرایش می‌کند (بار اول پین می‌شود). |
| `tgpm plan N [--dry-run]` | پیام پلن هفته‌ی N را پست یا ویرایش می‌کند؛ پلن‌های قدیمی از پین درمی‌آیند. |
| `tgpm sync` | همه‌ی پیام‌های پست‌شده را ویرایش می‌کند؛ وقتی هفته‌ی جاری کامل تیک خورد، هفته‌ی بعد را پست می‌کند. |
| `tgpm post` | پیام/فایل **جدید** به یک تاپیک می‌فرستد (`--topic`، `--text`، `--file`، `--document`، `--pin`، `--raw-html`، `--dry-run`). |
| `tgpm status` | پیشرفت را از فایل رودمپ چاپ می‌کند. |
| `tgpm agent install` | دستورالعمل tgpm را برای ابزارهای هوش مصنوعی نصب می‌کند (بخش ۳ب). |

گزینه‌ی کلی: `--dir <پوشه>` (پیش‌فرض پوشه‌ی جاری؛ `tgpm.json` به سمت بالا جست‌وجو می‌شود).

### ۵. تنظیمات (`tgpm.json`)

| کلید | معنی | پیش‌فرض |
|---|---|---|
| `project` | نام پروژه | نام پوشه |
| `hashtag` | هشتگ پیام‌ها (`""` یعنی هیچ) | نام بدون فاصله |
| `language` | `en` یا `fa` | `en` |
| `calendar` | `gregorian`، `jalali` یا `both` | `gregorian` |
| `roadmap_file` | مسیر فایل رودمپ | `ROADMAP.md` |
| `topics` | نام تاپیک‌ها بر اساس کلید: `roadmap`، `plan`، `updates` (برای `tgpm post --topic` کلید خودتان را اضافه کنید) | بسته به زبان |
| `max_item_len` | بیشینه‌ی طول متن هر کار در پیام | `120` |
| `advance` | با کامل شدن هفته‌ی جاری، هفته‌ی بعد خودکار پست شود | `true` |

شناسه‌ی پیام‌ها و تاپیک‌ها در `.tgpm/state.json` می‌ماند. اگر پیامی را در تلگرام پاک کردید، شناسه‌اش را از این فایل بردارید تا اجرای بعد پیام تازه بفرستد.

### ۶. ساخت فایل اجرایی

```powershell
powershell -File build_exe.ps1     # اول تست‌ها را اجرا می‌کند، بعد dist\tgpm.exe را با PyInstaller می‌سازد
```

فقط تست‌ها: `python -m unittest discover -s tests -t .`

### نکته‌ها و محدودیت‌ها

- tgpm فقط همان چیزی را می‌فرستد که شما بخواهید (`week`، `plan`، `sync`، `post`) و پیام‌های گروه را نمی‌خواند.
- توکن هیچ‌وقت در خروجی و خطاها نمی‌آید؛ در خطای شبکه فقط نوع خطا نشان داده می‌شود.
- پیام تلگرام حداکثر ۴۰۹۶ نویسه دارد. هفته‌های طولانی با «… و N مورد دیگر» کوتاه می‌شوند.
- ویرایشگرهای ویندوز ممکن است به `.env` و `tgpm.json` یک BOM اضافه کنند؛ tgpm هر دو را درست می‌خواند.

مجوز: MIT.
