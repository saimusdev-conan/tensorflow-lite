# tflite-conan
Tensorflow Lite Conan package

## Prerequisites

## Build

To build the Tensorflow Lite library with conan, run the following command:
```
conan create . tensorflow-lite/2.0.0@saimusdev/testing --profile=default --build=missing
```

### Debug build process
To increment the Conan's logging, increase the log level:
```
conan config set log.level=1
```
To avoid conan fetching the source each time use the ```--keep-source``` option when running ```conan create```:

```
conan create . tensorflow-lite/2.0.0@saimusdev/testing --profile=default --build=missing --keep-source
```
