const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');


var extractCSS = new ExtractTextPlugin({
	 filename: '[name].css'
});

module.exports = env => {
	if (env.CSS) return {
		context: path.join(__dirname, 'client/scss'),
		entry: {
			'base': './base.scss',
		},
		devtool: env.NODE_ENV == 'production' ? 'source-map' : 'inline-source-map',
		watch: env.NODE_ENV == 'production' ? false : true,
		output: {
			path: path.join(__dirname, 'build/css'),
			filename: '[name].css',
		},
		module: {
			rules: [
				{
					test: /\.scss$/,
					use: extractCSS.extract({
						use: [
							{
								loader: 'css-loader',
								options: {
									sourceMap: true,
									alias: {
										'../fonts': path.join(__dirname, '/node_modules/simple-line-icons/fonts')
									}
								}
							},
							{
								loader: 'postcss-loader',
								options: {
									sourceMap: true,
									ident: 'postcss',
									plugins: [
										require('autoprefixer'),
										require('cssnano')
									]
								}
							},
							{
								loader: 'sass-loader',
								options: {
									sourceMap: true,
									includePaths: [
										path.join(__dirname, 'node_modules/bootstrap/scss'),
										path.join(__dirname, 'node_modules/simple-line-icons/scss')
									]
								}
							}
						],
					})
				},
				{
					test: /\.(eot|svg|ttf|woff|woff2)$/,
					use: [
						{
							loader: 'file-loader',
							options: {
								name: '../fonts/[name].[ext]',
							}
						}
					]
				}
			]
		},
		plugins: [
			extractCSS,
		]
	}

	if (env.JS) return {
		context: path.join(__dirname, 'client/js'),
		entry: {
			'base': './base.js',
		},
		devtool: env.NODE_ENV == 'production' ? 'source-map' : 'inline-source-map',
		watch: env.NODE_ENV == 'production' ? false : true,
		output: {
			path: path.join(__dirname, 'build/js'),
			filename: '[name].js'
		},
		module: {
			rules: [
				{
					test: /\.js$/,
					exclude: /node_modules/,
					use: [
						{
							loader: 'babel-loader',
							options: {
								presets: ['@babel/preset-env']
							}
						}
					]
				}
			]
		}
};
}
