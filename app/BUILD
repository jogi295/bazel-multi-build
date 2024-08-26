# py_binary(
#     name = "even_odd_checker",
#     srcs = ["even_odd.py"],
#     main = "even_odd.py",
#     deps = [],
# )

py_binary(
    name = "even_odd_checker",
    srcs = ["even_odd.py"],
    # Optionally specify the main attribute if `even_odd.py` should be the entry point
    main = "even_odd.py",
    visibility = ["//:__pkg__"],  # Allows access from the root package
)
