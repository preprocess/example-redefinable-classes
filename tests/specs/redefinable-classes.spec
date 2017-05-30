--DESCRIPTION--

Test redefinable classes macros

--GIVEN--

class Child extends Parent implements One, Two, Three {
    public function hello() {
        print "world";
    }
}

class Child extends Parent implements One, Two, Three {

}

class Child extends Parent {

}

class Child {

}

new Child("foo", "bar");

new Child();

new Child;

--EXPECT--

\Pre\RedefinableClasses\define('Child', 'Parent', ['One', 'Two', 'Three'], 'cHVibGljIGZ1bmN0aW9uIGhlbGxvKCkgewogICAgICAgIHByaW50ICJ3b3JsZCI7CiAgICB9Cg==');

\Pre\RedefinableClasses\define('Child', 'Parent', ['One', 'Two', 'Three'], null);

\Pre\RedefinableClasses\define('Child', 'Parent', null, null);

\Pre\RedefinableClasses\define('Child', null, null, null);

\Pre\RedefinableClasses\resolve('Child', ["foo", "bar"]);

\Pre\RedefinableClasses\resolve('Child', []);

\Pre\RedefinableClasses\resolve('Child', null);
