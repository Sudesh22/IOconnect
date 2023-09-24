import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as GoIcons from 'react-icons/go';
import * as MdIcons from 'react-icons/md';
import * as PiIcons from "react-icons/pi";

export const SidebarData = [
  {
    title: 'Home',
    path: '/home',
    icon: <AiIcons.AiFillHome />,
    cName: 'nav-text'
  },
  {
    title: 'Dashboard',
    path: '/reports',
    icon: <MdIcons.MdDashboard />,
    cName: 'nav-text'
  },
  {
    title: 'Products',
    path: '/products',
    icon: <FaIcons.FaCartPlus />,
    cName: 'nav-text'
  },
  {
    title: 'Analytics',
    path: '/analytics',
    icon: <PiIcons.PiChartLineBold />,
    cName: 'nav-text'
  },
  {
    title: 'Team',
    path: '/team',
    icon: <IoIcons.IoMdPeople />,
    cName: 'nav-text'
  },
  {
    title: 'Notifications',
    path: '/messages',
    icon: <PiIcons.PiBellRingingBold />,
    cName: 'nav-text'
  },
  {
    title: 'Settings',
    path: '/settings',
    icon: <FaIcons.FaCogs />,
    cName: 'nav-text'
  },
  {
    title: 'Signout',
    path: '/support',
    icon: <GoIcons.GoSignOut />,
    cName: 'nav-text'
  }
];