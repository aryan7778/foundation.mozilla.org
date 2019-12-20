let webpack = require(`webpack`);
let path = require(`path`);
let frontendPath = path.resolve(
  __dirname,
  `network-api`,
  `networkapi`,
  `frontend`,
  `_js`
);

let rules = [
  {
    test: /\.js(x?)$/,
    exclude: /node_modules/,
    loader: `babel-loader`,
    query: {
      presets: [
        [`@babel/preset-env`, { targets: `> 1%, last 2 versions` }],
        [`@babel/preset-react`]
      ]
    }
  }
];

let main = (env) => {
  return {
    entry: `./source/js/main.js`,
    output: {
      path: frontendPath,
      filename: `main.compiled.js`
    },
    module: {
      rules
    },
    plugins: [
      new webpack.DefinePlugin({
        __SENTRY_DSN__: JSON.stringify(process.env.SENTRY_DSN),
        __HEROKU_RELEASE_VERSION__: JSON.stringify(
          process.env.HEROKU_RELEASE_VERSION
        ),
        __SENTRY_ENVIRONMENT__: JSON.stringify(process.env.SENTRY_ENVIRONMENT),
        __LOCAL_DEV__: env.local_dev
      })
    ]
  };
};

let bgMain = {
  entry: {
    "bg-main": `./source/js/buyers-guide/bg-main.js`,
    polyfills: `./source/js/polyfills.js`
  },
  output: {
    path: frontendPath,
    filename: `[name].compiled.js`
  },
  module: {
    rules
  }
};

module.exports = [main, bgMain];
