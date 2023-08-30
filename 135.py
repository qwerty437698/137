import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';

const HomeScreen = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Stars App</Text>
      <Text onPress={() => navigation.navigate('StarList')}>View Stars</Text>
    </View>
  );
};

const StarListScreen = () => {
  const [starData, setStarData] = useState([]);

  useEffect(() => {
    fetch('your_flask_api_url')
      .then(response => response.json())
      .then(data => setStarData(data))
      .catch(error => console.error(error));
  }, []);

  return (
    <ScrollView contentContainerStyle={styles.container}>
      {starData.map(star => (
        <View key={star.id}>
          <Text>{star.name}</Text>
          <Text>Mass: {star.mass}</Text>
          <Text>Radius: {star.radius}</Text>
          <Text>Distance: {star.distance}</Text>
          <Text>Gravity: {star.gravity}</Text>
        </View>
      ))}
    </ScrollView>
  );
};

const AppNavigator = createStackNavigator(
  {
    Home: HomeScreen,
    StarList: StarListScreen,
  },
  {
    initialRouteName: 'Home',
  }
);

export default createAppContainer(AppNavigator);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
});
