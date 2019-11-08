import nose


default_test_modules = ['pyoptools.tests.test_calc',
                        'pyoptools.tests.test_coding_standards',
                        'pyoptools.tests.test_components',
                        'pyoptools.tests.test_shapes',
                        ]


def run():
    nose.main(defaultTest=default_test_modules)

if __name__ == '__main__':
    run()