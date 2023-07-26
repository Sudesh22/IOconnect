import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as GoIcons from 'react-icons/go';
import * as MdIcons from 'react-icons/md';

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
    title: 'Team',
    path: '/team',
    icon: <IoIcons.IoMdPeople />,
    cName: 'nav-text'
  },
  {
    title: 'Notification',
    path: '/messages',
    icon: <IoIcons.IoIosNotifications />,
    cName: 'nav-text'
  },
  {
    title: 'Signout',
    path: '/support',
    icon: <GoIcons.GoSignOut />,
    cName: 'nav-text'
  }
];