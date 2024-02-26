Для работы демона в системе MacOS необходимо:
  1) Создать .plist файл по следующему шаблону:
      <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>com.example.script</string>
            <key>ProgramArguments</key>
            <array>
                <string>/path/to/your/script.sh</string>
            </array>
            <key>RunAtLoad</key>
            <true/>
            <key>StandardOutPath</key>
            <string>/path/to/your/logfile.log</string>
            <key>StandardErrorPath</key>
            <string>/path/to/your/error.log</string>
        </dict>
        </plist>
        *замените /path/to/your/* на актуальные пути
    2) Скопируйте .plist файл в папку launchd
    3) Загрузите скрипт в launchd используя комманду 'launchctl load /path/to/your/plistfile.plist'
