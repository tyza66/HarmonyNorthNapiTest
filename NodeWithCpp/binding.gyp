{
  "targets": [
    {
      "target_name": "addon",
      "sources": [ "native_addon.cpp" ],
      "include_dirs": [
  "<!(node -p \"path.join(__dirname, 'node_modules/node-addon-api')\")"
],

      "dependencies": [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      }
    }
  ]
}
