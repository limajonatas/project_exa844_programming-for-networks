import { api } from "../boot/axios";

export default {
  async getByGender() {
    const response = await api.get();
    return response.data.by_gender;
  },
  async getByRace() {
    const response = await api.get();
    return response.data.by_race;
  },
  async getByEducation() {
    const response = await api.get();
    return response.data.by_education_level;
  },
};
