#!/usr/bin/env ruby
puts ARGV[0].scan(/((?<=\[from:)\+?\w*(?=\]))|((?<=\[to:)\+?\w*(?=\]))|((?<=\[flags:)[-10:]*(?=\]))/).flatten.compact.join(",")