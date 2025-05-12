#include <napi.h>

Napi::Number Add(const Napi::CallbackInfo& info) {
    Napi::Env env = info.Env();

    double arg0 = info[0].As<Napi::Number>().DoubleValue();
    double arg1 = info[1].As<Napi::Number>().DoubleValue();

    return Napi::Number::New(env, arg0 + arg1);
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
    exports.Set(Napi::String::New(env, "add"), Napi::Function::New(env, Add));
    return exports;
}

NODE_API_MODULE(addon, Init);
