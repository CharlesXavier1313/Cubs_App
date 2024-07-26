import React from 'react';
import Odds from './Odds';

export default {
  title: 'Components/Odds',
  component: Odds,
};

const Template = (args) => <Odds {...args} />;

export const Default = Template.bind({});
Default.args = {
  // Add default props here
};
