#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostPtr_ContainerConan(base.BoostBaseConan):
    name = "boost_ptr_container"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_ptr_container"
    lib_short_names = ["ptr_container"]
    header_only_libs = ["ptr_container"]
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_circular_buffer",
        "boost_config",
        "boost_core",
        "boost_iterator",
        "boost_mpl",
        "boost_range",
        "boost_serialization",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_type_traits",
        "boost_unordered",
        "boost_utility"
    ]


