project('ara-icon-theme',
    version: '1.0',
    meson_version: '>= 0.40',
    license: 'CC-by-SA',
    default_options: ['prefix=/usr']
)

install_subdir('ara',
    install_dir: join_paths(get_option('prefix'), 'share/icons')
)

install_subdir('ara-dark',
    install_dir: join_paths(get_option('prefix'), 'share/icons')
)

meson.add_install_script('meson/post_install.py')
