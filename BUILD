filegroup(
    name = "app_files",
    srcs = glob(["app/**"]),
)

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = ["//app:even_odd_checker"],
)

