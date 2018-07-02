-- phpMyAdmin SQL Dump
-- version phpStudy 2014
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 服务器版本: 5.5.53
-- PHP 版本: 5.6.27
--
-- 数据库: `3618med`
--

-- --------------------------------------------------------

--
-- 表的结构 `logtable`
--

CREATE TABLE IF NOT EXISTS `logtable` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) DEFAULT NULL,
  `day` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `domain` varchar(255) DEFAULT NULL,
  `method` varchar(255) DEFAULT NULL,
  `uri` varchar(255) DEFAULT NULL,
  `http` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `datasize` int(11) DEFAULT NULL,
  `referer` varchar(255) DEFAULT NULL,
  `useragent` varchar(255) DEFAULT NULL,
  `cdnip` varchar(255) DEFAULT NULL,
  `md5str` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hs` (`md5str`) USING HASH
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
