#!/usr/bin/env ruby
from = ARGV[0].scan(/\[from:(\S+)\]/).flatten.first
to = ARGV[0].scan(/\[to:(\S+)\]/).flatten.first
flags = ARGV[0].scan(/\[flags:(\S+)\]/).flatten.first

puts "#{from},#{to},#{flags}"

