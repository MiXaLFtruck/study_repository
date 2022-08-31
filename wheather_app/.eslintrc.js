module.exports = {
    "env": {
        "browser": true,
        "es2021": true,
    },
    "extends": [
        "eslint:recommended",
        "plugin:react/recommended",
				"airbnb/base",
    ],
    "overrides": [
    ],
    "parserOptions": {
        "ecmaVersion": "latest",
        "sourceType": "module",
				"ecmaFeatures": {
					"jsx": true,
				},
    },
    "plugins": [
        "react",
    ],
    "rules": {
			"no-tabs": 0,
			"indent": 0,
			"quotes": [2, "double", { "avoidEscape": true, "allowTemplateLiterals": true }],
			"quote-props": [2, "as-needed", { "unnecessary": false }],
			"class-methods-use-this": ["error", { "exceptMethods": ["render"] }],
			"react/prop-types": 0,
			"global-require": 0,
			"comma-dangle": 0,
    },
		"globals": {
			"Atomics": "readonly",
			"SharedArrayBuffer": "readonly",
		},
};
