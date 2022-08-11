const gulp = require('gulp');
const postcss = require('gulp-postcss');
const postcss_combine_duplicated_selectors = require('postcss-combine-duplicated-selectors');
const postcss_discard_duplicates = require('postcss-discard-duplicates');
const postcssPresetEnv = require('postcss-preset-env');
const autoprefixer = require('autoprefixer');
const postcssOverflowShorthand = require('postcss-overflow-shorthand');

const postcssPlugins = [
  postcss_combine_duplicated_selectors({}),
  postcss_discard_duplicates(),
  postcssPresetEnv(),
  autoprefixer({}),
  postcssOverflowShorthand(),
];

gulp.task('css', () => {
  return gulp.src('./src/app/**/*.css').pipe(postcss(postcssPlugins)).pipe(gulp.dest('./src/app'));
});

gulp.task('scss', () => {
  return gulp.src('./src/app/**/*.scss').pipe(postcss(postcssPlugins)).pipe(gulp.dest('./src/app'));
});

gulp.task('default', gulp.series('scss', 'css'));
