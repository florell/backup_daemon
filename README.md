How to use on MacOS?
1) Create .plist file using this template (change /path/to/your/* to actual paths)
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
3) Copy .plist file to launchd dir
4) Load script into launchd using command:
    ```launchctl load /path/to/your/plistfile.plist```
